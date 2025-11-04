import streamlit as st
from streamlit_ace import st_ace

with st.container():
    q1 = st.markdown('`Q1: Create a new Conda environment named "myenv" with Python 3.12.`')
    a1 = st_ace(language='sh', height=20, theme='terminal', key='conda_a1')

    if 'conda create -n myenv python=3.12' in a1:
        st.success('Correct! That creates an environment called myenv with Python 3.12.')

with st.container():
    q2 = st.markdown('`Q2: Activate the environment "myenv".`')
    a2 = st_ace(language='sh', height=20, theme='terminal', key='conda_a2')

    if 'conda activate myenv' in a2:
        st.success('Correct! The environment is now active.')

with st.container():
    q3 = st.markdown('`Q3: Install numpy and pandas into the currently active environment.`')
    a3 = st_ace(language='sh', height=20, theme='terminal', key='conda_a3')

    if ('conda install numpy pandas' in a3) or ('mamba install numpy pandas' in a3):
        st.success('Correct! Packages will be installed into the active env.')

with st.container():
    q4 = st.markdown('`Q4: On Apple Silicon, create an x86_64 environment named "python-x64" with Python 3.12.`')
    a4 = st_ace(language='sh', height=20, theme='terminal', key='conda_a4')

    if 'conda create --platform osx-64 --name python-x64 python=3.12' in a4:
        st.success('Correct! This targets the x86_64 platform on macOS.')

with st.container():
    q5 = st.markdown('`Q5: Export the current environment to environment.yml.`')
    a5 = st_ace(language='sh', height=20, theme='terminal', key='conda_a5')

    if ('conda env export > environment.yml' in a5) or ('conda env export -f environment.yml' in a5):
        st.success('Correct! This captures the environment specification.')

with st.container():
    q6 = st.markdown('`Q6: Export an explicit package list (exact build pins) to spec-file.txt.`')
    a6 = st_ace(language='sh', height=20, theme='terminal', key='conda_a6')

    if 'conda list --explicit > spec-file.txt' in a6:
        st.success('Correct! The explicit list can fully reproduce the environment on the same platform.')

with st.container():
    q7 = st.markdown('`Q7: Create an environment from environment.yml.`')
    a7 = st_ace(language='sh', height=20, theme='terminal', key='conda_a7')

    if ('conda env create -f environment.yml' in a7) or ('conda env update -f environment.yml' in a7):
        st.success('Correct! env create (or update) reads the YAML file.')

with st.container():
    q8 = st.markdown('`Q8: Create an environment named myenv from an explicit spec file spec-file.txt.`')
    a8 = st_ace(language='sh', height=20, theme='terminal', key='conda_a8')

    if 'conda create --name myenv --file spec-file.txt' in a8:
        st.success('Correct! The explicit spec recreates exact builds for the same platform.')

with st.container():
    q9 = st.markdown('`Q9: You broke your env. Show revisions and roll back to revision 3.`')
    a9 = st_ace(language='sh', height=40, theme='terminal', key='conda_a9')

    if ('conda list --revisions' in a9) and ('conda install --revision 3' in a9):
        st.success('Correct! Inspect revisions, then roll back using install --revision.')

with st.container():
    q10 = st.markdown('`Q10: Remove the environment named "myenv" completely.`')
    a10 = st_ace(language='sh', height=20, theme='terminal', key='conda_a10')

    if ('conda env remove -n myenv' in a10) or ('conda remove --name myenv --all' in a10):
        st.success('Correct! That removes the environment and its packages.')

with st.container():
    q11 = st.markdown('`Q11: Prefer the faster dependency solver. Configure Conda to use libmamba.`')
    a11 = st_ace(language='sh', height=20, theme='terminal', key='conda_a11')

    if 'conda config --set solver libmamba' in a11:
        st.success('Correct! libmamba is generally faster than the classic solver.')
    elif 'conda config --set solver classic' in a11:
        st.warning('This switches back to the classic solver. The question asked for libmamba.')

with st.container():
    q12 = st.markdown('`Q12: Install openslide version 4.0.0 from conda-forge channel.`')
    a12 = st_ace(language='sh', height=20, theme='terminal', key='conda_a12')

    if ('conda install -c conda-forge openslide=4.0.0' in a12) or ('mamba install -c conda-forge openslide=4.0.0' in a12):
        st.success('Correct! Using conda-forge ensures the package comes from that channel.')

with st.container():
    q13 = st.markdown('`Q13: Which of the following are good practices? (Select all that apply)`')
    g1 = st.checkbox('Do not reuse one env for multiple unrelated projects', key='conda_g1')
    g2 = st.checkbox('Export environment after submissions or stable milestones', key='conda_g2')
    g3 = st.checkbox('Use git to version large datasets directly', key='conda_g3')
    g4 = st.checkbox('Use explicit spec files when cross-host reproducibility is critical', key='conda_g4')

    if g1 and g2 and g4 and not g3:
        st.success('Correct! Avoid reusing envs, export envs, and use explicit specs. Large data should not live in Git; consider git-lfs, or object stores.')
    elif g3:
        st.error('Versioning large files directly in Git is discouraged. Consider git-lfs/object stores instead.')
