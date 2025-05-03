/* @refresh reload */
import {render} from 'solid-js/web'
import {Navigate, Route, Router, Routes} from "@solidjs/router";
import Index from './index.jsx'
import ComingSoon from "./ComingSoon.jsx";

const root = document.getElementById('root')

if (import.meta.env.DEV && !(root instanceof HTMLElement)) {
    throw new Error('Root element not found. Did you forget ' +
        'to add it to your index.html? Or maybe the id attribute got misspelled?')
}

function Redirect() {
    return <Navigate href={`/2025`}/>
}

render(() => (
    <Router>
        <Routes>
            <Route path="/" component={Redirect}/>
            <Route path="/2025" component={Index}/>
            <Route path="/2025/coming-soon" component={ComingSoon}/>
        </Routes>
    </Router>
), root)
