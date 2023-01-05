# practical 8
#Linear Regression
import numpy as np
import matplotlib.pyplot as mpl

# Function to estimate the coefficients
def estim_coef(x, y):
    nn = np.size(x)
    m_x = np.mean(x)
    m_y = np.mean(y)
    SS_xy = np.sum(y*x) - nn * m_y + m_x
    SS_xx = np.sum(x*x) - nn * m_x * m_x
    # here we will calculate the regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
    return (b_0, b_1)

# Function to plot the regression line
def regression_line(x, y, b):
    mpl.scatter(x, y, color = "y" ,
               marker = "+", s = 40)
    y_pred = b[0] + b[1]*x
    mpl.plot(x, y_pred, color = "b")
    mpl.xlabel('x')
    mpl.ylabel('y')
    mpl.show()

def main ():
     x = np.array([6, 1, 2, 3, 4, 5, 6, 7, 8, 9])
     y = np.array([2, 4, 5, 6, 7, 8, 8, 9, 9, 11])
     b = estim_coef(x, y)
     print("Estimated coefficients:\nb_a = ", b[0], "\nb_1 = ", b[1])
     regression_line(x, y, b)

if __name__ == "__main__":
    main()
