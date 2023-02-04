from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation

fig = plt.figure()
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')

#df_2 = pd.read_excel("3D_plot_sorted1.xlsx")
#df_2 = pd.read_excel("loss_hist_train3.xlsx")
df_2 = pd.read_excel("loss_hist_full_data_set_(train+valid)_2.xlsx")
datafile_2 = df_2.values                  ## stored data from xlsx file
scaler_datafile_2 = (datafile_2)

n0 = scaler_datafile_2[:,0]   ## rf power
n1 = scaler_datafile_2[:,1]    ## fsr
n2 = scaler_datafile_2[:,2]     ## ex
n3 = scaler_datafile_2[:,3]     ## freq

n4 = scaler_datafile_2[:,4]     ## time index
n5 = scaler_datafile_2[:,6]     ## MSE loss
#display(n5)
n6 = (scaler_datafile_2[:,12])     ## pred_freq
#display(n6)
n7 = scaler_datafile_2[:,13]     ## cons_real
n8 = scaler_datafile_2[:,14]     ## cons_pred
n9 = scaler_datafile_2[:,15]     ## des_real
n10 = scaler_datafile_2[:,16]     ## cons_pred

#print(y)
tri = Triangulation(np.ravel(n0), np.ravel(n3))

ax = plt.axes(projection ='3d')
# ax.plot_trisurf(n3, n0, n4, label = "Cons_real", triangles = tri.triangles, cmap ='Greens', linewidths = 0.2);
# ax.plot_trisurf(n3, n0, n5, label = "Cons_predicted", triangles = tri.triangles, cmap ='Reds', linewidths = 0.2);
# ax.plot_trisurf(n3, n0, n6, label = "Des_real", triangles = tri.triangles, cmap ='Blues', linewidths = 0.2);
# ax.plot_trisurf(n3, n0, n7, label = "Des_predicted", triangles = tri.triangles, cmap ='Greys', linewidths = 0.2);

ax.plot_trisurf(n3, n0, n7, label = "Cons_real", triangles = tri.triangles, cmap ='Greens', linewidths = 0.2);
ax.plot_trisurf(n3, n0, n8, label = "Cons_predicted", triangles = tri.triangles, cmap ='Reds', linewidths = 0.2);
ax.plot_trisurf(n3, n0, n9, label = "Des_real", triangles = tri.triangles, cmap ='Blues', linewidths = 0.2);
ax.plot_trisurf(n3, n0, n10, label = "Des_predicted", triangles = tri.triangles, cmap ='Greys', linewidths = 0.2);
# ax.legend (['a'], ['a'], ['a'], ['a'])

# plot_color_gradients('Perceptually Uniform Sequential', ['viridis', 'plasma', 'inferno', 'magma', 'cividis'])
# plot_color_gradients('Sequential',['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu','GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'])
# rotate the image
ax.view_init(20, 40)
fig

ax.set_xlabel('Frequency (GHz)', rotation=0, labelpad=50)
ax.set_ylabel('RF power (dBm)', rotation=0, labelpad=50)
ax.set_zlabel('Opt. Power (dBm)', rotation=0, labelpad=50)
# ax.grid(False)

                