import subprocess
import time

Z = 0.275

def set_pose(name, x, y, z=Z):
    cmd = (
        "gz service -s /world/default/set_pose "
        "--reqtype gz.msgs.Pose "
        "--reptype gz.msgs.Boolean "
        "--timeout 1000 "
        f"--req 'name: \"{name}\" position {{ x: {x:.2f} y: {y:.2f} z: {z:.3f} }}'"
    )
    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# 2 humans: move through middle horizontal corridor, left <-> right
h1_x = 1.0
h2_x = 11.0
h1_dir = 1
h2_dir = -1

# 5 humans: one in each vertical aisle, bottom <-> top
aisle_x = [1.0, 3.0, 5.0, 7.0, 9.0]
aisle_y = [-5.8, 5.8, -5.8, 5.8, -5.8]
aisle_dir = [1, -1, 1, -1, 1]

while True:
    # Middle corridor humans at y=0.
    # They move left-right from opposite directions.
    h1_x += 0.04 * h1_dir
    h2_x += 0.04 * h2_dir

    if h1_x >= 11.0:
        h1_dir = -1
    if h1_x <= 1.0:
        h1_dir = 1

    if h2_x >= 11.0:
        h2_dir = -1
    if h2_x <= 1.0:
        h2_dir = 1

    set_pose("human_vertical_1", h1_x, 0.25)
    set_pose("human_vertical_2", h2_x, -0.25)

    # Aisle humans.
    # They move bottom-top only in safe x corridors,
    # avoiding shelf centers x=2,4,6,8,10.
    for i in range(5):
        aisle_y[i] += 0.035 * aisle_dir[i]

        if aisle_y[i] >= 5.8:
            aisle_dir[i] = -1
        if aisle_y[i] <= -5.8:
            aisle_dir[i] = 1

        set_pose(f"human_aisle_{i+1}", aisle_x[i], aisle_y[i])

    time.sleep(0.04)