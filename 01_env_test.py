import robosuite as suit
import numpy as np

def main():
    env  = suit.make(
        env_name="Lift",
        robots="Panda",
        has_renderer = True,
        has_offscreen_renderer = False,
        use_camera_obs= False,
        control_freq =20,
    )

    obs  = env.reset()

    print("observation keys:",obs.keys())
    print("action dimension:",env.action_dim)

    for step in range(500):
        action =  np.random.randn(env.action_dim) *0.1
        obs,reward,done,info = env.step(action)

        env.render()

        if step %100 == 0:
            print("step:", step, "reward:", reward, "done:", done)

    env.close()

if __name__ == "__main__":
    main()



    