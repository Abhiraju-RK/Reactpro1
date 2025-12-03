import { userState } from 'react';
import AddStudent from './components/AddStudent';
import StudentList from './components/StudentList';

function App(){
  const [students,setstudents]=userState([]);
  const addStudent=(student)=>{
    setstudents([...students,student])

  };
  return(
    <div className='container'>
      <h1>React Pro - Student Management</h1>
      <AddStudent addStudent={addStudent}
    </div>
  )
}
