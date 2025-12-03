import { useState } from "react";

function AddStudent({addStudent}){
    const [name,setName]=useState('');
    const [course, setCourse]=useState('');

    const handleSubmit=(e)=>{
        e.preventDefault();

        if (!name || !course){
            alert('please fill the fields!!');
            return;
        }

        addStudent({name,course});
        setName('');
        setCourse('');
    };
    
    return (
        <form onSubmit={handleSubmit}>
            <h1></h1>
        </form>
    )
}