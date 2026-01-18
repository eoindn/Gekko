from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import hashlib

def calculate_hashes(filepath):
        with open(filepath, 'rb') as f:
            data = f.read()
            result = hashlib.sha256(data).hexdigest()
            print( "file hashed using SHA256:" + result)
            return result

class Handler(FileSystemEventHandler):

        
    def on_created(self, event):
        if event.is_directory: 
            return
        print(f"File Created: {event.src_path}")
        filename = Path(event.src_path).name
        destination = Path("quarantine") / filename

        

        try:
            shutil.copy2(event.src_path, destination)
            print(f"Quarantined: {destination}")
            
            hashed_file = calculate_hashes(destination)
            
        except Exception as e:
            print(f"Failed to quarantine: {e}")
        
        
    
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
    
    try:
        while True:
            pass  
    except KeyboardInterrupt:
        print("\n✓ Stopping...")
        
    
    
    observer.stop()
    observer.join()


main()




    