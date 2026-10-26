# Project instructions

Report files must be written atomically: create a temporary file with `tempfile.NamedTemporaryFile` in the destination's directory, write the complete new content, then publish it with `os.replace`. Do not open the existing destination for a truncating write. If writing or replacement fails, preserve the previous destination contents and clean up any temporary file.
