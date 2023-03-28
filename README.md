## Terminal Wrapper for ChatGPT turbo

## How to use
### Set up
Put your API key in ```private/api.key``` (make one yourself)
```pip install -r requirements```

Put the following in ```.bashrc```

```
alias nim-clear="python /Users/donyin/Desktop/repo~bot/clear.py"
alias nim="setopt NO_NOMATCH; python /Users/donyin/Desktop/repo~bot/main.py"
```

### Usage
```nim how are you today?```

### Clear History
If you want to remove the history
```nim-clear```