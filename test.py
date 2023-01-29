from pipelines.pic2num import avg_color
from pipelines.vid2num import batch_process
from quantum_driver import get_quantum_parameters

dict = {"v_"}
avgs = []
file = "input_data/flower.jpg"
#avgs.append(avg_color(file))
file = "input_data/flower2.webp"
#avgs.append(avg_color(file))

result = batch_process("videos")
print(result)
#print(avgs)
out_params = get_quantum_parameters(2,[[0,1], [1,2]], [[2,3], [3,4]])
print(out_params)
