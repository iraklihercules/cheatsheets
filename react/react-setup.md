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
