import {useEffect, useState} from "react";

export default function App() {

    const [advice, setAdvice] = useState("");
    const [counter, setCounter] = useState(0);

    async function getAdvice() {
        const response = await fetch("https://api.adviceslip.com/advice");
        const data = await response.json();
        setAdvice(data.slip.advice);
        setCounter(c => c + 1);
    }

    /**
     * This function is executed when the component is loaded.
     * Don't forget to add an empty array at the end.
     */
    useEffect(() => {
        /**
         * Strict Mode
         *
         * <React.StrictMode> renders components twice (on dev but not production) in order to detect
         * any problems with your code and warn you about them (which can be quite useful).
         *
         * To remove the strict mode (not recommended), change the code from this
         *
         * root.render(
         *   <React.StrictMode>
         *     <App />
         *   </React.StrictMode>
         * );
         *
         * to this
         *
         * root.render(
         *     <App />
         * );
         */
        getAdvice();
    }, []);

    return (
        <>
            <h1>{advice}</h1>
            <button onClick={getAdvice}>Get Advice</button>
            <p>You have read <strong>{counter}</strong> advices.</p>
            <Message counter={counter} />
        </>
    );
}

/**
 * Component
 */
function Message({ counter })  {
    return (
        <p>You have read <strong>{counter}</strong> advices.</p>
    );
}
