import matplotlib.pyplot as plt
def liang_barsky(x1, y1, x2, y2, xwmin, ywmin, xwmax, ywmax):
    dx = x2 - x1
    dy = y2 - y1
    tmin = 0.0
    tmax = 1.0
    p = [-dx, dx, -dy, dy]
    q = [x1 - xwmin, xwmax - x1, y1 - ywmin, ywmax - y1]
    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                tmin = max(tmin, t)
            else:
                tmax = min(tmax, t)
    if tmin > tmax:
        return None
    x_clip1 = x1 + tmin * dx
    y_clip1 = y1 + tmin * dy
    x_clip2 = x1 + tmax * dx
    y_clip2 = y1 + tmax * dy
    return (x_clip1, y_clip1), (x_clip2, y_clip2)
def plot_clipping(x1, y1, x2, y2, xwmin, ywmin, xwmax, ywmax, clipped_line=None):
    fig, ax = plt.subplots()
    plt.plot([x1, x2], [y1, y2], label='Original Line', color='blue', linestyle='--')
    rect = plt.Rectangle((xwmin, ywmin), xwmax - xwmin, ywmax - ywmin, 
                         edgecolor='red', facecolor='none', label='Clipping Window')
    ax.add_patch(rect)
    if clipped_line:
        (x_clip1, y_clip1), (x_clip2, y_clip2) = clipped_line
        plt.plot([x_clip1, x_clip2], [y_clip1, y_clip2], label='Clipped Line', color='green')
    plt.xlim(min(x1, x2, xwmin) - 10, max(x1, x2, xwmax) + 10)
    plt.ylim(min(y1, y2, ywmin) - 10, max(y1, y2, ywmax) + 10)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Liang-Barsky Clipping Algorithm')
    plt.legend()
    plt.grid(True)
    plt.show()
def get_user_input():
    print("Enter the coordinates for the line segment")
    x1 = float(input("x1 "))
    y1 = float(input("y1 "))
    x2 = float(input("x2 "))
    y2 = float(input("y2 "))
    print("Enter the coordinates for the clipping window")
    xwmin = float(input("xwmin (left boundary) "))
    ywmin = float(input("ywmin (bottom boundary) "))
    xwmax = float(input("xwmax (right boundary) "))
    ywmax = float(input("ywmax (top boundary) "))
    return x1, y1, x2, y2, xwmin, ywmin, xwmax, ywmax
x1, y1, x2, y2, xwmin, ywmin, xwmax, ywmax = get_user_input()
clipped_line = liang_barsky(x1, y1, x2, y2, xwmin, ywmin, xwmax, ywmax)
plot_clipping(x1, y1, x2, y2, xwmin, ywmin, xwmax, ywmax, clipped_line)
