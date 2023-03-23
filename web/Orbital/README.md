# Orbital

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: In order to decipher the alien communication that held the key to their location, she needed access to a decoder with advanced capabilities - a decoder that only The Orbital firm possessed. Can you get your hands on the decoder?

## NOTES

1. Deploy Docker
   1. > IP:
2. Extract files
   1. > unzip web_orbital.zip
      1. FILE(S): docker setup / website files
3. Looking at the code we see a particular line that stands out

    ```py
        def exportFile():
            if not request.is_json:
                return response('Invalid JSON!'), 400
            
            data = request.get_json()
            communicationName = data.get('name', '')

            try:
                # Everyone is saying I should escape specific characters in the filename. I don't know why.
                return send_file(f'/communications/{communicationName}', as_attachment=True)
            except:
                return response('Unable to retrieve the communication'), 400
    ```

4. This tells me that we might be able to upload a file that was not intended/safe to upload
