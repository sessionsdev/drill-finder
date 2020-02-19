import React, { Component } from "react";
import axios from "axios";
import { Route, Switch } from "react-router-dom";
import Modal from 'react-modal';

import About from "./components/About";
import NavBar from "./components/NavBar";
import FindDrillForm from './components/FindDrillForm';
import Message from './components/Message';

Modal.setAppElement(document.getElementById("root"));

const modalStyles = {
  content: {
    top: '0',
    left: '0',
    right: '0',
    bottom: '0',
    border: 0,
    background:'transparent'
  }
};

class App extends Component {
  constructor() {
    super();
    this.state = {
      drills: [],
      title: "Drill Finder",
      messageType: null,
      messageText: null,
      showModal: false
    };
  }
  componentDidMount() {
    this.getDrills();
  }

  handleOpenModal = () => {
    this.setState({ showModal: true });
  };
  
  handleCloseModal = () => {
    this.setState({ showModal: false });
  };


  getDrills() {
    axios
    .get(`${process.env.REACT_APP_WEB_SERVICE_URL}/drills`)
    .then(res => {
      this.setState({drills: res.data });
      console.log(res)
    })
    .catch(err => {
      console.log(err);
    });

  }
  


  handleFindDrillFormSubmit = (data) => {
    const url = `${process.env.REACT_APP_WEB_SERVICE_URL}/drills/find-drill`
    axios.post(url, data)
      .then((res) => {
        console.log(res)
      })
    console.log("Sanity check!")
  }


  createMessage = (type, text) => {
    this.setState({
      messageType: type,
      messageText: text,
    });
    setTimeout(() => {
      this.removeMessage();
    }, 3000);
  };

  removeMessage = () => {
    this.setState({
      messageType: null,
      messageText: null,
    });
  };



  render() {
    return (
      <div>
        <NavBar 
        title={this.state.title} 
        />
        <section className="section">
          <div className="container">
            {this.state.messageType && this.state.messageText &&
            <Message
              messageType={this.state.messageType}
              messageText={this.state.messageText}
              removeMessage={this.removeMessage}
            />
            }
            <div className="columns">
              <div className="column is-half">
                <br />
                <Switch>
                <Route exact path="/" render ={() => (
                    <div>
                      <h1 className="title is-1">Drill Finder</h1>
                    </div>
                )}
                />
                <Route exact path="/find-drill" render={() => (
                  <FindDrillForm
                    handleFindDrillFormSubmit={this.handleFindDrillFormSubmit} 
                  />
                )} 
                />
              
                <Route exact path="/about" component={About} />
                </Switch>
              </div>
            </div>
          </div>
        </section>
      </div>
    );
  }
}

export default App;