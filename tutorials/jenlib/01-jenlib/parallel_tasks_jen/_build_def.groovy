@Library("jenlib@master") _

jenlib.ci-flow(
"""
# --- @@[name=autobuild.yaml, state=start, target.name=parallel_tasks_jen]
name: parallel_tasks_jen
taskfile: ./Taskfile.yml
taskentry: ci-flow
# --- @@[name=autobuild.yaml, state=end]
""")
