import streamlit as st
from streamlit_ace import st_ace

with st.container():
    q1 = st.markdown('`Q1: Run an interactive Ubuntu container and open a shell. Auto-remove when it exits.`')
    a1 = st_ace(language='sh', height=20, theme='terminal', key='docker_a1')

    if ('docker run --rm -it ubuntu sh' in a1) or ('docker run --rm -it ubuntu bash' in a1):
        st.success('Correct! You are now inside a temporary Ubuntu container.')

with st.container():
    q2 = st.markdown('`Q2: Build an image from the current directory and tag it myimage:latest.`')
    a2 = st_ace(language='sh', height=20, theme='terminal', key='docker_a2')

    if ('docker build . -t myimage:latest' in a2) or ('docker build -t myimage:latest .' in a2):
        st.success('Correct! That builds and tags the image.')

with st.container():
    q3 = st.markdown('`Q3: Run a container from myimage exposing container port 80 on host port 8080.`')
    a3 = st_ace(language='sh', height=20, theme='terminal', key='docker_a3')

    if ('docker run -p 8080:80 myimage' in a3) or ('docker run --publish 8080:80 myimage' in a3):
        st.success('Correct! Host 8080 maps to container 80.')

with st.container():
    q4 = st.markdown('`Q4: Mount the host directory ./data as read-only at /app/data inside the container.`')
    a4 = st_ace(language='sh', height=20, theme='terminal', key='docker_a4')

    if ('-v ./data:/app/data:ro' in a4) or ('--volume ./data:/app/data:ro' in a4):
        st.success('Correct! The directory is mounted read-only.')

with st.container():
    q5 = st.markdown('`Q5: Write a minimal Dockerfile for a Python app that:`\n- uses `python:3.11-slim`\n- sets `WORKDIR /app`\n- copies `requirements.txt` and installs it\n- copies the source (`./app`)\n- starts with: `python app.py`')
    a5 = st_ace(language='dockerfile', height=180, theme='terminal', key='docker_a5')

    has_from = 'FROM python:3.11-slim' in a5
    has_workdir = 'WORKDIR /app' in a5
    has_copy_req = ('COPY requirements.txt /app' in a5) or ('COPY requirements.txt .' in a5)
    has_run_pip = ('RUN pip install -r requirements.txt' in a5)
    has_copy_src = ('COPY . /app' in a5) or ('COPY . .' in a5)
    has_cmd = ('CMD ["python", "app.py"]' in a5) or ('CMD ["python","app.py"]' in a5) or ('CMD python app.py' in a5)

    if has_from and has_workdir and has_copy_req and has_run_pip and has_copy_src and has_cmd:
        st.success('Correct! That is a solid minimal Python Dockerfile.')

with st.container():
    q6 = st.markdown('`Q6: Write a docker-compose.yml service named web that:`\n- builds from `.`\n- maps `8080:80`\n- mounts `./data` to `/app/data` (rw)\n- restarts `unless-stopped`')
    a6 = st_ace(language='yaml', height=160, theme='terminal', key='docker_a6')

    cond_service = 'web:' in a6
    cond_build = ('build:' in a6) and ('.' in a6)
    cond_ports = ('ports:' in a6) and ('- "8080:80"' in a6 or '- 8080:80' in a6)
    cond_vol = ('volumes:' in a6) and ('- ./data:/app/data' in a6)
    cond_restart = 'restart: unless-stopped' in a6

    if cond_service and cond_build and cond_ports and cond_vol and cond_restart:
        st.success('Correct! That compose service meets all requirements.')

with st.container():
    q7 = st.markdown('`Q7: List all running containers and then all containers including stopped ones.`')
    a7 = st_ace(language='sh', height=40, theme='terminal', key='docker_a7')

    if ('docker ps' in a7) and ('docker ps -a' in a7):
        st.success('Correct! ps shows running; ps -a shows all.')

with st.container():
    q8 = st.markdown('`Q8: Show logs from a running container named api and follow the output.`')
    a8 = st_ace(language='sh', height=20, theme='terminal', key='docker_a8')

    if ('docker logs -f api' in a8) or ('docker logs --follow api' in a8):
        st.success('Correct! That tails the container logs.')

with st.container():
    q9 = st.markdown('`Q9: Exec into a running container named db with an interactive bash shell.`')
    a9 = st_ace(language='sh', height=20, theme='terminal', key='docker_a9')

    if 'docker exec -it db bash' in a9:
        st.success('Correct! You are executing an interactive shell in db.')

with st.container():
    q10 = st.markdown('`Q10: Write a multi-stage Dockerfile that builds a wheel and copies it into a slim runtime image.`')
    a10 = st_ace(language='dockerfile', height=220, theme='terminal', key='docker_a10')

    has_stage1 = ('FROM python' in a10) and ('AS builder' in a10)
    has_build = ('WORKDIR /build' in a10) and ('RUN pip wheel -w dist .' in a10 or 'pip wheel' in a10)
    has_stage2 = ('FROM python' in a10) and ('COPY --from=builder' in a10)

    if has_stage1 and has_build and has_stage2:
        st.success('Correct! That captures the essence of a multi-stage build.')

with st.container():
    q11 = st.markdown('`Q11: Prune all unused images, containers, and networks without prompts.`')
    a11 = st_ace(language='sh', height=20, theme='terminal', key='docker_a11')

    if 'docker system prune -af' in a11:
        st.success('Correct! That force-prunes unused artifacts.')

with st.container():
    q12 = st.markdown('`Q12: In compose, how do you declare an environment variable SOME_VAR=some_value for the service web?`')
    a12 = st_ace(language='yaml', height=100, theme='terminal', key='docker_a12')

    if ('environment:' in a12) and ('SOME_VAR: "some_value"' in a12 or 'SOME_VAR: some_value' in a12):
        st.success('Correct! environment key sets service variables.')

with st.container():
    q13 = st.markdown('`Q13: Your app is not reachable in the browser. What should you double-check? (Select all that apply)`')
    c1 = st.checkbox('Port mapping in docker run / compose', key='docker_c1')
    c2 = st.checkbox('Container is running and healthy', key='docker_c2')
    c3 = st.checkbox('App is bound to 0.0.0.0 inside container', key='docker_c3')
    c4 = st.checkbox('Hostname in image FROM line', key='docker_c4')

    if c1 and c2 and c3 and not c4:
        st.success('Correct! Check port mapping, container status, and bind address.')
    elif c4:
        st.error('The base image hostname is unrelated. Focus on ports, health, and bind address.')

with st.container():
    q14 = st.markdown('`Q14: Define a compose stack with two services web and redis where web depends_on redis.`')
    a14 = st_ace(language='yaml', height=160, theme='terminal', key='docker_a14')

    cond_redis = 'redis:' in a14
    cond_web = 'web:' in a14
    cond_dep = 'depends_on:' in a14 and ('- redis' in a14 or 'redis:' in a14)

    if cond_redis and cond_web and cond_dep:
        st.success('Correct! The dependency is declared in compose.')

with st.container():
    q15 = st.markdown('`Q15: Push an image myimage:latest to Docker Hub under user myuser.`')
    a15 = st_ace(language='sh', height=40, theme='terminal', key='docker_a15')

    has_tag = ('docker tag myimage:latest myuser/myimage:latest' in a15) or ('docker tag myimage myuser/myimage:latest' in a15)
    has_push = 'docker push myuser/myimage:latest' in a15
    if has_tag and has_push:
        st.success('Correct! Tag with namespace, then push to the registry.')

with st.container():
    q15 = st.markdown('`Q16: Expert question, do not use any outside help! You built a linux/amd64 image using a linux/amd64 base image on your Apple Silicon. Trying to pull this image on linux/amd64 produces an error, stating that the image is not available for your target system, although it is linux/amd64. Where did you go wrong? (Hint: "Buying a Mac" is not the answer)`')
    a15 = st_ace(language='sh', height=40, theme='terminal', key='docker_a16')

    if '--platform=linux/amd64' in a15:
        st.success('Correct! The correct meta information will otherwise be missing from the docker manifest.')
