import robosuite as suite
import numpy as np

def make_action(env,move_xyz,gripper):
    action = np.zeros(env.action_dim)

    action[:3] = move_xyz
    action[-1]=gripper

    return action

def main():
    env =suite.make(
        env_name="Lift",
        robots = "Panda",
        has_renderer = True,
        has_offscreen_renderer=False,
        use_camera_obs=False,
        use_object_obs=True,
        control_freq=20,
    )
    obs = env.reset()

    print("obs keys:")
    for key in obs.keys():
        print(key)
    print ("action dimensions :",env.action_dim)

    for step in range(700):
        cube_pos = obs["cube_pos"]
        eef_pos = obs["robot0_eef_pos"]
        move_xyz = np.zeros(3)


        if step <200 :
            target_pos = cube_pos.copy()
            target_pos[2] += 0.05
            
            
            direction = target_pos - eef_pos
            move_xyz[:3] = direction[:3] * 2

            move_xyz = np.clip(move_xyz ,-0.05,+0.05)

            gripper = -1
        
        elif step <350 :
            target_pos = cube_pos.copy()
            target_pos[2] += 0.001

            direction = target_pos - eef_pos
            move_xyz[:3] = direction[:3] 

            move_xyz = np.clip(move_xyz ,-0.02,+0.02)

            gripper = -1

        elif step < 450 : 
            move_xyz = np.array([0,0,-0.05])

            gripper = 1
        
        else :
            move_xyz = np.array([0,0,0.05])

            gripper =1

        action = make_action(env,move_xyz,gripper)

        obs,reward,done,info = env.step(action)
        env.render()

        if step % 50 == 0:
            print("step:", step)
            print("cube_pos:", cube_pos)
            print("eef_pos:", eef_pos)
            print("cube height:", cube_pos[2])
            print("reward:", reward)
            print("done:", done)
            print("-" * 40)

        

        


            


    
    env.close()



if __name__ == "__main__":
    main()