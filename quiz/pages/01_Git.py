import streamlit as st
from streamlit_ace import st_ace

with st.container():

    q1 = st.markdown('`Q1: How do you initiate a Git repository from the commandline?`')
    a1 = st_ace(language='sh', height=20, theme='terminal', key='a1')

    if 'git init' in a1:
        st.success('Correct! You can now find a (hidden) `.git` folder in the repository root')

with st.container():
    q2 = st.markdown('`Q2: You now have a local repository. How can you add a file "hello.txt" to git?`')
    a2 = st_ace(language='sh', height=20, theme='terminal', key='a2')

    match a2:
        case 'git add hello.txt':
            st.success('Correct! Your file was added!')

        case 'git add --all':
            st.warning('Close, you might be adding other files in your working directory!')

        case 'git add -A':
            st.warning('Close, you might be adding other files in your working directory!')

with st.container():
    q3 = st.markdown('`Q3: Which "area" was this file now added to?`')
    a3_1 = st.checkbox('My working directory')
    a3_2 = st.checkbox('The staging area')
    a3_3 = st.checkbox('My local repository')
    a3_4 = st.checkbox('The remote repository')

    if a3_1 or a3_3 or a3_4:
        st.error('Try again.')

    elif a3_2:
        st.success('Correct!')

with st.container():
    q4 = st.markdown('`Q4: How do you create a commit with the message "Initial commit"?`')
    a4 = st_ace(language='sh', height=20, theme='terminal', key='a4')

    if ('git commit -m "Initial commit"' in a4) or ("git commit -m 'Initial commit'" in a4):
        st.success('Correct! Your first commit is created.')

with st.container():
    q5 = st.markdown('`Q5: How do you add a remote named "origin" pointing to https://example.com/user/repo.git?`')
    a5 = st_ace(language='sh', height=20, theme='terminal', key='a5')

    if 'git remote add origin https://example.com/user/repo.git' in a5:
        st.success('Correct! Remote "origin" is configured.')

with st.container():
    q6 = st.markdown('`Q6: How do you push the current branch (main) to origin and set upstream tracking?`')
    a6 = st_ace(language='sh', height=20, theme='terminal', key='a6')

    if ('git push -u origin main' in a6) or ('git push --set-upstream origin main' in a6):
        st.success('Correct! Upstream tracking is set.')

with st.container():
    q7 = st.markdown('`Q7: How do you clone https://example.com/user/repo.git into a folder named "myproj"?`')
    a7 = st_ace(language='sh', height=20, theme='terminal', key='a7')

    if 'git clone https://example.com/user/repo.git myproj' in a7:
        st.success('Correct! The repository will be cloned into "myproj".')

with st.container():
    q8 = st.markdown('`Q8: How do you create and switch to a new branch called feature/login?`')
    a8 = st_ace(language='sh', height=20, theme='terminal', key='a8')

    if ('git checkout -b feature/login' in a8) or ('git switch -c feature/login' in a8):
        st.success('Correct! You are on the new branch.')

with st.container():
    q9 = st.markdown('`Q9: You are on main. How do you merge the branch feature/login into main?`')
    a9 = st_ace(language='sh', height=20, theme='terminal', key='a9')

    if 'git merge feature/login' in a9:
        st.success('Correct! The branch is merged into main (conflicts permitting).')

with st.container():
    q10 = st.markdown('`Q10: Undo the last commit but keep all changes STAGED. Which command?`')
    a10 = st.radio('Choose one', [
        'git reset --hard HEAD~1',
        'git reset --mixed HEAD~1',
        'git reset --soft HEAD~1'
    ], key='a10')

    if a10 == 'git reset --soft HEAD~1':
        st.success('Correct! --soft keeps changes staged.')
    elif a10 in ['git reset --hard HEAD~1', 'git reset --mixed HEAD~1']:
        st.error('Not quite. --mixed unstages, --hard discards changes.')

with st.container():
    q11 = st.markdown('`Q11: Show a compact commit graph for all branches in the terminal.`')
    a11 = st_ace(language='sh', height=20, theme='terminal', key='a11')

    if ('git log --oneline --graph --all' in a11) or ('git log --graph --oneline --all' in a11):
        st.success('Correct! That shows a concise graph across branches.')

with st.container():
    q12 = st.markdown('`Q12: Save your uncommitted changes temporarily and then apply the most recent stash without dropping it.`')
    a12 = st_ace(language='sh', height=40, theme='terminal', key='a12')

    if ('git stash save' in a12 or 'git stash push' in a12) and ('git stash apply' in a12):
        st.success('Correct! Use stash save/push, then apply without dropping.')
