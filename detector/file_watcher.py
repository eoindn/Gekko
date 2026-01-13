from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    
    def on_created(self,event):
        if event.is_directory:
            return
        print(f"File Created: {event.src_path}")
    
    def on_deleted(self,event):
        if event.is_directory:
            return
        print(f"File Deleted: {event.src_path}")
    
    def on_modified(self,event):
        if event.is_directory:
            return
        print(f"File Modified: {event.src_path}")

   
   
def main():
    path = Path("testfolder")
    observer = Observer()
    handler = Handler()
    observer.schedule(handler, path, recursive=True)
    observer.start()
    
    while True:
        cmd = input("> ")
        if cmd == "q":
            break
    observer.stop()
    observer.join()


main()




    