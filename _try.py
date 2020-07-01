try:
    import index
except:
    import traceback
    with open('error.txt', 'w') as f:
        f.write(traceback.format_exc())