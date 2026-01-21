from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import hashlib
import json
from datetime import datetime
def calculate_hashes(filepath):
        with open(filepath, 'rb') as f:
            data = f.read()
            result = hashlib.sha256(data).hexdigest()
            print( "file hashed using SHA256:" + result)
            return result
        
        
def add(json_data):
    
    try:  
        with open("logs/quarantine_log.json", "r") as file:
            logs = json.load(file) 
        
        logs.append(json_data)
        
        with open("logs/quarantine_log.json", "w") as file:
            json.dump(logs, file, indent=2)
 

    except (FileNotFoundError, json.JSONDecodeError):

        logs = []  
        logs.append(json_data)
        with open("logs/quarantine_log.json", "w") as file:
            json.dump(logs, file, indent=2)

          
    
    
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
            file_size = destination.stat().st_size 
            timestamp = datetime.now().isoformat() 
            string_original_path = str(Path(event.src_path))
            string_destination = str(destination)
            json_data = {
                
                "timestamp": timestamp,
                "filename": filename,
                "original_path" : string_original_path,
                "quarantine_path":  string_destination,
                "sha256" : hashed_file,
                "file_size": file_size 
                
            }
            add(json_data)
            
            
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




    