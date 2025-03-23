import { useState } from "react";

function Button() {
  const [inform, setinform] = useState({
    Username:"",
    Password:""
  });

  const click = () => {
    alert(`Username: ${inform.Username} \nPassword: ${inform.Password}`);

  };

  const change = (event) => {
    const {name,value} = event.target
    setinform({...inform,[name]:value})
    console.log(inform)
  };

  return (
    <>
      <div>
        <input type="text" 
        value={setinform.Username}
        name="Username"
        placeholder="Username"
        onChange={change}
        />
      </div>
      <div>
        <input type="password"
        value={setinform.Password}
        name="Password"
        placeholder="Password"
        onChange={change}
        />
      </div>

      <div>
        <button className="btn" onClick={click}>
          <p className="btntext">Summit</p>
        </button>
      </div>
    </>
  );
}

export default Button;
