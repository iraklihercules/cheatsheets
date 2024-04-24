import React from "react"
import ReactDOM from "react-dom/client"

function App() {
    return (
        <>
            <h1>Hello World!</h1>
            <MyComponent />
        </>
    );
}

function MyComponent() {
    return <h2>My Component</h2>
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);
