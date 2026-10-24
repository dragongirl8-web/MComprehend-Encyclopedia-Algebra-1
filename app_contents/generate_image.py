import matplotlib.pyplot as plt
import numpy as np


def generate_line_chart():
    x = np.array([1, 2, 3, 4])
    y = x * 2

    # Create line chart
    plt.plot(x, y)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Simple Line Chart")
    plt.savefig("C:\\Users\\drago\\OneDrive\\Documents\\StarStudent\\Star Student\\MComprehend Encyclopedia Algebra 1\\app_contents\\static\\images\\line_chart.png")

if __name__ == "__main__":
    generate_line_chart()
