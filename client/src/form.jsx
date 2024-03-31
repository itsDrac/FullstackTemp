import { useState } from 'react';
import API from './api.jsx';

function AddHeroForm() {
	const [ formData, setFormData] = useState({
		name: '',
		realName: '',
		description: '',
	});

	const [toShow, setToShow] = useState(false);
	const [message, setMessage] = useState('');

	const handleChange = (event) => {
		setFormData({
			...formData,
			[event.target.name]: event.target.value,
		});
	}

	const handleSubmit = async (event) => {
		event.preventDefault();
		API.post('/create', formData, {
			headers: {
				'Content-Type': 'application/json'
			},
			withCredentials: true
		})
		.then(res => {
			console.log(res)
			setMessage(res.data.message);
			setToShow(true);
		})
		.catch(err => {
			console.log("Cant add hero ", err.response.data.detail)
			setMessage(err.response.data.detail);
			setToShow(true);
		});

	};


	return (
		<>
		<h3 style={{ "visibility": `${toShow}` }}>{message}</h3>
		<form onSubmit={handleSubmit}>
			<label htmlFor="name">
				Name : 
				<input
					type="text"
					id="name"
					name="name"
					value={formData.name}
					onChange={handleChange}
				/>
			</label>
		<br/>
			<label htmlFor="realName">
				Real Name : 
				<input
					type="text"
					id="realName"
					name="realName"
					value={formData.realName}
					onChange={handleChange}
				/>
			</label>
		<br/>
			<label htmlFor="description">
				Description : 
				<textarea
					id="description"
					name="description"
					rows="3"
					value={formData.description}
					onChange={handleChange}
				/>
			</label>
		<br/>
		<button type="submit"> Add </button>
		</form>
		</>
	);
}

export default AddHeroForm;
