@nrp.MapSpikeSink("cortex_out", nrp.brain.ctx_M1_layers[1], nrp.leaky_integrator_alpha)
@nrp.Robot2Neuron()
def c_brainbody (t):
    clientLogger.info('out :', cortex_out.voltage)
