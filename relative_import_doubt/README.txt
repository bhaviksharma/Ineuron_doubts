AIM:
I want to import package from parent directory. Please run the .py file which is in parent_dir directory.

MY TRIALS:
Link I referred for this issue: # https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time/14132912#14132912
I also tried creating __init__.py in the folders, but id doesn't help.
I also tried creating system variable manually, it also didn't help.
I would like relative import to work. Even if 3rd option works, I am not interested in it because we have to do it everytime for every project, it is also problematic to share across because somebody else has to set the environment variable again for a basic task.

INFO:
__package__ : return none.
Whatever module we work in is __main__ hence it has no parent pacakge. This is what I could deduct from above link.
I have included the Import error image.I 
