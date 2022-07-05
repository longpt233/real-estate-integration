import {memo} from "react";

export const Select = memo(({name, data, defaultValue, onChange, keyName})=>{
    const changeSelect = (event)=>{
        onChange(keyName, event.target.value)
    }
    return (
        <div>
            <div className="filter-item">
                <select className="form-select" aria-label="Default select example" onChange={(changeSelect)}>
                    <option selected value={defaultValue}>{name}</option>
                    {data.map((item, index)=><option key={index} value={item}>{item}</option>)}
                </select>
            </div>
        </div>
    )
})
