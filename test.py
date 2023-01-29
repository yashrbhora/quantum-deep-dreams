from pipelines.pic2num import avg_color
from quantum_driver import get_quantum_parameters

file = "input_data/flower.jpg"
avg = avg_color(file)
print(avg)
out_params = get_quantum_parameters(2,{0:avg})
print(out_params)
