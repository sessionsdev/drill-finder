import React from 'react';
import PropTypes from 'prop-types';
import { Formik } from 'formik';
import * as Yup from 'yup';


import './form.css';

const FindDrillForm = (props) => {
    return (
        <div>
            <h1 className="title is-1">Find Drill</h1>
            <hr /><br />
            <Formik
                initialValues={{
                    diameter: '',
                    depth:'',
                    material: '',
                    machine: ''
                }}
                onSubmit={(values, { setSubmitting, resetForm}) => {
                    props.handleFindDrillFormSubmit(values);
                    resetForm();
                    setSubmitting(false);
                }}
            >
                {props => {
                    const {
                        values,
                        touched,
                        errors,
                        isSubmitting,
                        handleChange,
                        handleBlur,
                        handleSubmit,
                    } = props;
                    return (
                        <form onSubmit={handleSubmit}>
                            <div className="field">
                                <label htmlFor="input-diameter" className="label">
                                    Diameter
                                </label>
                                <input
                                    name="diameter"
                                    id="input-diameter"
                                    className={
                                        errors.diameter && touched.diameter
                                          ? "input error"
                                          : "input"
                                      }
                                    type="text"
                                    placeholder="Enter diameter"
                                    value={values.diameter}
                                    onChange={handleChange}
                                    onBlur={handleBlur}
                                />
                            </div>
                            <div className="field">
                                <label htmlFor="input-depth" className="label">
                                    Depth
                                </label>
                                <input
                                    name="depth"
                                    id="input-depth"
                                    className={
                                        errors.depth && touched.depth
                                          ? "input error"
                                          : "input"
                                      }
                                    type="text"
                                    placeholder="Enter depth"
                                    value={values.depth}
                                    onChange={handleChange}
                                    onBlur={handleBlur}
                                />
                            </div>
                            <input 
                                type="submit"
                                className="button is-primary"
                                value="Submit"
                                disabled={isSubmitting}
                            />
                        </form>
                    )
                }}

            </Formik>
                
        </div>
    )
}

export default FindDrillForm;