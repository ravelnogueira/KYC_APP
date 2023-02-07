import { BrowserRouter, Route, Routes } from 'react-router-dom'
import BuscaMaps from './views/BuscaMaps/BuscaMaps'
import ConsultaCliente from './views/ConsultaCpf/ConsultaCpf'
import HomePage from './views/HomePage/HomePage'
import Layout from './components/Layout/Layout'
import ConsultaSituacaoCadastral from './views/ConsultaSituacaoCadastral/ConsultaSituacaoCadastral'

function Router() {
    return (
        <BrowserRouter>
            <Routes>
            <Route element={<Layout />}>
                <Route path='/*' element={<HomePage/>}/>
                <Route path='/buscamaps' element={<BuscaMaps />} />
                <Route path='/pesquisaportaltransparencia' element={<ConsultaCliente />} />
                <Route path='/consultasituacaocadastral' element={<ConsultaSituacaoCadastral/>}/>
            </Route>
            </Routes>
        </BrowserRouter>)
}

export default Router