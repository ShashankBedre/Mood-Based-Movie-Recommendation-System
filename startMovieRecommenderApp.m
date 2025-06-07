function startFlaskApp()
    % Set Python environment (if needed)
    % pyenv('Version', 'path_to_python.exe');
    
    % System command to run app.py
    system('python app.py &');
    
    disp('Flask app started successfully!');
end
