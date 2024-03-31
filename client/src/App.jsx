import './App.css';
import AddHeroForm from './form.jsx';
import API from './api.jsx';
function App() {
	function ping() {
		console.log("clicked")
		API.get('/ping').then(res => {
			console.log(res)
		})
	}
	return (
	<>
		<button onClick={ping}>Ping</button>
		<h1>Add Heros</h1>
		<AddHeroForm />
	</>
  )
}

export default App
