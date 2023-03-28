## Terminal Wrapper for ChatGPT turbo


https://user-images.githubusercontent.com/65135356/228243450-4eac489e-ab68-44df-b3a4-a71faea67a84.mov


## How to use
### Set up
Put your API key in ```private/api.key``` (make one yourself)
```pip install -r requirements```

Put the following in your ```.bashrc```

```
alias nim-clear="python {your abs path to}/clear.py"
alias nim="setopt NO_NOMATCH; python {your abs path to}/main.py"
```

### Usage
```nim how are you today?```

### Clear History
If you want to remove the history
```nim-clear```
