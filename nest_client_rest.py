from nest_client import NESTClient
import requests
import json

def encode(response):
    if response.ok:
        return response.json()
    else:
        raise requests.exceptions.HTTPError(response.status_code)


class NESTClientREST(NESTClient):

    recorders = {}

    def __init__(self, host='localhost', port=5000):
        self.url = 'http://{}:{}/'.format(host, port)
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


    def __getattr__(self, call):
        def method(*args, **kwargs):
            kwargs.update({'args': args})
            response = requests.post(self.url + 'api/' + call, json=kwargs, headers=self.headers)
            return encode(response)
        return method

    # TODO: christopher parameter ignored by GetKernelStatus if passed as input paramenter
    def get_kernel_status(self, parameter):
#        return self._nest_srvapi('GetKernelStatus')['response']['data'][parameter]
        # TODO: christopher what about ['response']['data'], are they needed in some cases?
        return self.GetKernelStatus(parameter)


    def startup(self, num_processes, num_threads_per_process, resolution, min_delay, max_delay):
        if num_processes < 1:
            raise ValueError('startup(): num_processes must be >= 1. Aborting.')
        if num_processes > 1:
            raise ValueError('startup(): Distributed execution (i.e. num_processes > 1) '
                             'not implemented yet.')

        self.ResetKernel()

        self.SetKernelStatus(params={
            "local_num_threads": num_threads_per_process,
            "resolution": resolution,
            "min_delay": min_delay,
            "max_delay": max_delay,
        })


    def load_network(self, filename):

        with open(filename) as script:
            script_source = script.read()

        json_dict = {
            'source': script_source,
            'return': ['populations']
        }

        response = requests.post(self.url + 'exec', json=json_dict, headers=self.headers)
        return(encode(response)['data']['populations'])


    def run_simulation(self, duration):
        if 0 <= duration <= ((2**32-1) // 2):
            self.Simulate(t=duration)
        else:
            print('run_simulation(): duration has to be between 0 and (2**32-1)/2.')


    # TODO: what about a function instead of a class method?
    def create_device(self, device_model, n=1, parameters=None):
        params = {'model' : device_model,
                  'n' : n,
                  'params' : parameters }
#        return self._nest_srvapi('Create', params)['response']['data']
        return self.Create(model=device_model, n=n, params=parameters)

    # TODO: what about a function instead of a class method?
    def connect_device(self, device, direction, neurons,
                       conn_spec=None, syn_spec=None, model=None):
        if direction == 'device_to_neuron':
            params = {'pre': device, 'post': neurons,
                      'conn_spec': conn_spec, 'syn_spec': syn_spec}
#                      'model': model}
            #            nest.Connect(device, nest.NodeCollection(neurons),
            #                         conn_spec, syn_spec, model)
        else:
            params = {'pre': neurons, 'post': device,
                      'conn_spec': conn_spec, 'syn_spec': syn_spec}
#                      'model': model}
            #            nest.Connect(nest.NodeCollection(neurons), device,
            #                         conn_spec, syn_spec, model)

#        self._nest_srvapi('Connect', params)
        self.Connect(**params)


    # TODO: Why is this not in nest_client_import? Who's using this?
    def get_population_parameters(self, population):
        celltype = self.GetStatus(nodes=population)['model'][0]
        return self.GetDefaults(model=celltype)


    # TODO: can we generalize the connect_device method in order to include this one?
    def connect_source_to_generator(self, source, generator):
        self.connect_device(source, generator)


    # TODO: this function partially duplicates the register_device one but in NRP they are split 
    def register_recorder(self, device, recordable=None):
        device = device.tolist()
        # TODO: christopher re-activate the check
        # if device_info['type'] == 'recorder':
        #     self.recorders[device[0]] = device_info['recordable']
        self.recorders[device[0]] = recordable


    def register_device(self, device_type, neurons):

        dev = self.get_device_info(device_type)
        device = self.Create(model=dev["model"], n=1, params=dev["parameters"])

        if dev['direction'] == 'device_to_neuron':
            params = {'pre': device, 'post': neurons}
        else:
            params = {'pre': neurons, 'post': device}
        self.Connect(**params)

        if dev['type'] == 'recorder':
            self.recorders[device[0]] = dev['recordable']

        return device


    def delete_device(self, device):
        pass


    def set_device_params(self, device, parameters):
        self.SetStatus(nodes=device, params=parameters)


    def get_device_data(self, device):
        response = self.GetStatus(nodes=device)[0]

        if device[0] in self.recorders:
            response = self.recorders[device[0]](response)
        return response


    def get_status(self, nodes, keys=None):
        params = {'nodes': nodes,
                  'keys': keys}
        return self._nest_srvapi('GetStatus',params)['response']['data']


    def finalize(self):
        pass
