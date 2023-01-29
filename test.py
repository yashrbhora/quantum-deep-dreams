from pipelines.pic2num import avg_color
from quantum_driver import get_quantum_parameters

dict = {"v_"}
avgs = []
file = "input_data/flower.jpg"
avgs.append(avg_color(file))
file = "input_data/flower2.webp"
avgs.append(avg_color(file))
print(avgs)
out_params = get_quantum_parameters(2,[[0,1], [1,2]], [[2,3], [3,4]])
print(out_params)
