import signac
import numpy as np
import unyt as u

def init_project():

    # Initialize project
    project = signac.init_project("gromacs_nvt1x1x1-1nm_1-layer")

    # Define temperature
    temperature = 298.0 * u.K

    # Start with a few different number of waters in the pore
    nwaters = [1, 23, 24]

    for nwater in nwaters:
        if nwater == 1:
            nsteps = 100000000
        else:
            nsteps = 50000000
        # Define the state point
        state_point = {
            "T": float(temperature.in_units(u.K).value),
            "nwater": nwater,
            "nsteps": nsteps,
        }

        job = project.open_job(state_point)
        job.init()


if __name__ == "__main__":
    init_project()
