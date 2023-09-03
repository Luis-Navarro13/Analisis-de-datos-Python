import numpy as np
import matplotlib.pyplot as plt
#definiendo variables
x= np.arange(0,20,0.1) #definiendo la variable de masa
y= np.arange(-15,15,0.1) #definiendo la variable de la altura en cm
#malla para crear la funcion
xx, yy = np.meshgrid(x,y)
#x se junta con todos los valores de y
#y se junta con todos los valores de x

#Evaluacion de la funcion m/h**2
u=2 * np.sin(2*np.pi*xx/20) - np.cos(2*np.pi*yy/20) #ecuacion del bmi

mycmap = plt.get_cmap('plasma',30)
niveles=(-1,0,1)
plt.figure() #Crea una grafica
graf_malla = plt.pcolormesh(xx,yy,u,cmap=mycmap) 
graf_cont = plt.contour(xx,yy,u,niveles,colors='black',linewidths=3)
barracol = plt.colorbar(graf_malla) #Hace que el mesh tenga color
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Grafica [m]')
barracol.ax.set_ylabel('altura',fontsize=11)

plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(xx,yy,u,color='peru')
ax.set_xlabel('valores x')
ax.set_ylabel('valores y')
ax.set_zlabel('valores z')


#eje proyeccion tridimensional
#haz la grafica de alambres con los valores