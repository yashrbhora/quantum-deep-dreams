# Import moviepy editor library, which gives us the editing functions
from moviepy.editor import *
import numpy as np

sample_dict = [{0: 0.89, 1: 0.94, 2: 0.92, 3: 0.33, 4: 0.01, 5: 0.24, 6: 0.12, 7: 0.04}]
sample_dict = [{0: 0.4906688912615728, 1: 0.5093311087384271, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.49707823632106757, 1: 0.5029217636789325, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.5002453827276924, 1: 0.4997546172723076, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.4934513127403871, 1: 0.5065486872596129, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.42379314752595154, 1: 0.5762068524740485, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.5007961458644445, 1: 0.49920385413555546, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.48575225819851703, 1: 0.5142477418014829, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.49779169126144257, 1: 0.5022083087385574, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.4916817025038838, 1: 0.5083182974961162, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.4265161542447965, 1: 0.5734838457552035, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.39946799156781193, 1: 0.6005320084321881, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.5045010145645552, 1: 0.4954989854354447, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.5323237873222143, 1: 0.46767621267778575, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.5753095281556725, 1: 0.4246904718443276, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.570518141117878, 1: 0.429481858882122, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.5515588782497756, 1: 0.4484411217502245, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.4999827475580253, 1: 0.5000172524419747, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.500283956610887, 1: 0.4997160433891131, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.49999012317338093, 1: 0.5000098768266191, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.503623782061481, 1: 0.4963762179385191, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.5008456737144037, 1: 0.49915432628559625, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.5007562508790668, 1: 0.49924374912093306, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.46877311456189413, 1: 0.5312268854381058, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.4056654193221038, 1: 0.5943345806778961, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.4680253434632974, 1: 0.5319746565367026, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}, {0: 0.4958837405165112, 1: 0.5041162594834888, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}]
sample_dict = [{0: 0.22634539178517596, 1: 0.00028668479910600006, 2: 0.0, 3: 0.0, 4: 0.70643459538972, 5: 0.5941097690026609}, {0: 0.05265138549379534, 1: 6.180744008729201e-05, 2: 0.7436905264192042, 3: 0.8496208442769838, 4: 0.6226555389972185, 5: 0.9148995041893255}, {0: 0.030963451631485624, 1: 0.0016900575368020835, 2: 0.9889730010332495, 3: 0.9813026064616152, 4: 0.807141853716769, 5: 0.434847074376378}, {0: 0.022204013977962404, 1: 0.0141255576296324, 2: 0.8716533253922882, 3: 0.9682283952441502, 4: 0.18749205829874951, 5: 0.5519105810103263}, {0: 0.022608306018120004, 1: 0.03813258643821999, 2: 0.5344359185268502, 3: 0.9591405031765003, 4: 0.6259666734230802, 5: 0.9922747022070004}, {0: 0.004292441839938, 1: 0.18021754542683802, 2: 0.5368482452035309, 3: 0.9719938381575001, 4: 0.40738410514320594, 5: 0.3980449541268661}, {0: 2.9850911014200002e-05, 1: 0.46872545629346374, 2: 0.7906549454172617, 3: 0.98418137433058, 4: 0.7934776489977742, 5: 0.38762554612302585}, {0: 0.000104939974449187, 1: 0.96603665162035, 2: 0.5126956061253214, 3: 0.8869434634373224, 4: 0.7310216929767734, 5: 0.21327247086285236}, {0: 0.0015682426020850004, 1: 0.9508959411267603, 2: 0.19096371017665104, 3: 0.5858555676437148, 4: 0.9585167779203403, 5: 0.11207117846452498}, {0: 0.002908152438328, 1: 0.6798659668469951, 2: 0.054031048263878, 3: 0.35181726145001213, 4: 0.46328430438120005, 5: 0.064127156787078}, {0: 0.036892864105949635, 1: 0.5104309051644089, 2: 0.05735848903418304, 3: 0.099428263043873, 4: 0.25993240246348953, 5: 0.05168657544486599}, {0: 0.9969428813209997, 1: 0.4404243988640001, 2: 0.21230448260605, 3: 0.017517535375089998, 4: 0.4991453591509, 5: 0.027091372143690003}, {0: 0.9785939074999997, 1: 0.8301225941699998, 2: 0.49576772684599985, 3: 0.04721040221, 4: 0.3674288435449999, 5: 0.03641917277000001}, {0: 0.8229027090381561, 1: 0.9977481500650642, 2: 0.9092868365414397, 3: 0.0792645327621265, 4: 0.0493039072977456, 5: 0.0865946801632796}, {0: 0.6183821884483298, 1: 0.7240942665571799, 2: 0.9147665476606, 3: 0.11026939118372002, 4: 0.20790790370127002, 5: 0.14037127459285997}, {0: 0.3909283894064, 1: 0.8909561290190001, 2: 0.8780546962860001, 3: 0.0967958583188, 4: 0.07205836316980001, 5: 0.5466027708151001}, {0: 0.3165728915825477, 1: 0.9574669488702864, 2: 0.03001597198544961, 3: 0.5221166696277525, 4: 0.9999970703383151, 5: 0.9892211598618975}, {0: 0.48634260851683553, 1: 0.9954603814083002, 2: 0.6802559763899535, 3: 0.28591001825917906, 4: 0.364135843636684, 5: 0.9816147410549301}, {0: 0.3776405863955381, 1: 0.8564809578521924, 2: 0.9670281339895521, 3: 0.5945597930602905, 4: 0.446262773251651, 5: 0.830715948239508}, {0: 0.5822618470702001, 1: 0.98200442504, 2: 0.9374758608339999, 3: 0.48893896260380004, 4: 0.5298939453041001, 5: 0.4348470763137}, {0: 0.9994609012914001, 1: 0.8746252967576801, 2: 0.7179529821357681, 3: 0.9355706975795111, 4: 0.760775468064301, 5: 0.4085107780496575}, {0: 0.91658654738, 1: 0.72301243656, 2: 0.159723723935, 3: 0.9489650955200002, 4: 0.6457044810760001, 5: 0.36181104477500003}, {0: 0.30519340117800003, 1: 0.13742557840700007, 2: 0.15269981243700007, 3: 0.9429650498299997, 4: 0.9955629475999997, 5: 0.326347379424}, {0: 0.33191686402432996, 1: 0.07636810271792, 2: 0.14580591544962004, 3: 0.8710785661278998, 4: 0.985752769453, 5: 0.41901827236555994}, {0: 0.5856281463490864, 1: 0.32550616764848944, 2: 0.21428585746200848, 3: 0.764542571159101, 4: 0.9880811146030198, 5: 0.41901826215515503}, {0: 0.7066904332266088, 1: 0.8598565611946198, 2: 0.2263128458701899, 3: 0.5683692078414748, 4: 0.9197846773505, 5: 0.89943365846737}]
sample_dict = [{key : val / sum(sample_dict_dist.values()) for key, val in sample_dict_dist.items()} for sample_dict_dist in sample_dict]
print("DICT:", sample_dict)

# Function to read the file of opacity inputs
def read_input():
    # Defining and array of the opacity levels for each clip
    opacities = []
    # Iterates through file inputs
    for i in range(len(sample_dict[0])):
        # Parses the input format and stores in variable
        placeholder = sample_dict[0][i]
        # Appends list of video opacities with appropriate float
        opacities.append(placeholder)
    # Finally, returns our array of opacities
    return opacities
# Initializes list of video clips
videos = []
# Takes list of opacity levels from input function
opacities = read_input()
# Iterates through videos and assigns opacities
for i in range(len(opacities)):
    # Initializes video clip from file
    videos.append(VideoFileClip("video_" + str(i+1) + ".mp4"))
    # Sets the opacity level of the video
    videos[i] = videos[i].set_opacity(opacities[i])
# Combines our array of videos into a composite clip
final_video = CompositeVideoClip(videos)
# Writes our final video to a .webm file
final_video.write_videofile("final_video.mp4")