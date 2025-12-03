import { userState } from 'react';
import AddStudent from './components/AddStudent';
import StudentList from './components/StudentList';

function App(){
  const [students,setStudents]=userState([]);
  const addStudent=(student)=>{
    setStudents([...students,student])

  };
  return(
    <div className='container'>
      <h1>React Pro - Student Management</h1>
      <AddStudent addStudent={addStudent} />
      <StudentList students={students} />
    </div>
  )
}

export default App;