import ReactDOM from "react-dom";
import {BrowserRouter, Routes, Route, Navigate} from "react-router-dom";
import {House} from "./pages/House/House";
import store from "./service/redux";
import { Provider } from 'react-redux'

function App(){
    return(
        <BrowserRouter>
            <div className="App">
                <Routes>
                    <Route path="index" element={<House/>}></Route>
                </Routes>
            </div>
        </BrowserRouter>
    )
}

export default App
if (document.getElementById('app')) {
    ReactDOM.render(<Provider store={store}><App /></Provider>, document.getElementById('app'));
}
