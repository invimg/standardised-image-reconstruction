from tests.reconstruction_algorithms.test_baseline_delay_and_sum import TestDelayAndSum
import matplotlib.pyplot as plt

out = TestDelayAndSum("TestDelayAndSum")
out.p_factor = 1.5
out.fnumber = 0.5
out.test_delay_and_sum_reconstruction_is_running_through()
out.test_delay_and_sum_reconstruction_is_running_through_fnumber()
out.test_delay_and_sum_reconstruction_is_running_through_pDAS()

# On peut utiliser la classe PDAS avec p=1 et un fnumber
#out.p_factor = 1
#out.test_delay_and_sum_reconstruction_is_running_through_pDAS()

plt.show()
