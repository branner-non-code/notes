## Git Merge — Version Controlled CI and CD — Deploying with Git Instead of Scripts — Sytse "Sid" Sijbrandij

In the future, we can avoid using different kinds of tools for these processes: container images and container schedulers. Examples of container schedulers are Kubernetes, Apache Mesos, Docker Swarm. Container images will likely be generated from a Dockerfile.

Build artifcacts are not enough, since Docker containers have layers.

Git hosts should also be container registries. Then there can be one docker file for all different environments, and different environments will be layered.

Container scheduling should go up and down with one's workload — since our load varies dramatically, we created GitLab Runner Autoscale (the poor person's scheduler). 

[end]