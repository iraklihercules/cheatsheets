# React Setup

1. Create new project
```bash
$ npm create vite@latest
# project name: . (current directory)
# Choose React
# Choose TypeScript
```

2. In the package.json specify the port
```json
{
  "scripts": {
    "dev": "vite --port 8080 --host"
  }
}
```

## Rules
Components:
1. When we write components as functions, they must start with uppercase letter.
2. The function needs to return some markup.
