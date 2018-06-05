import React, { Component } from 'react';
import { connect } from 'react-redux';
import { createStudent } from '../../Actions/studentPage'
import './JoinRace.css';
import { Button, Form, FormGroup, Input, InputGroup, InputGroupButtonDropdown, DropdownToggle, DropdownItem, DropdownMenu, Label } from 'reactstrap';

// still need to add functionality
// also will need to map over the availble teams for the dropdown menu

class StudentJoinCard extends Component {
    constructor(props){
        super(props);
        this.state = {
            name: '',
            team: null,
        //     teams: this.props.teams,
        //     raceName: this.props.raceName,
        //     randomTeams:this.props.randomTeams,
        //     dropdownOpen: false,

        };
        // this.handleClick = this.handleClick.bind(this);
        // this.select =this.select.bind(this);
        // this.onChange=this.onChange.bind(this);
        // this.toggleDropDown = this.toggleDropDown.bind(this);
    }
    componentDidMount() {
        // this.props.gettingRace(this.props.match.params.slug)
    }

    // toggleDropDown = () => {
    //     this.setState({
    //       dropdownOpen: !this.state.dropdownOpen
    //     });
    //   }

    onChange = (e) => {
        this.setState({ [e.target.name]: e.target.value});
    }

    select = (e) => {
        this.setState({ [e.target.name]: e.target.value})
    }
    
    handleClick = (e) => {
        e.preventDefault();
        let slug = this.props.slug
        let history = this.props.history
        console.log(this.state)
        this.props.createStudent(this.state, slug, history)
        //this.props.studentJoinRace(this.state);
    }

    render() {
        // const randomTeams =this.state.randomTeams;
        return(
            this.props.gotRace ?
            <div>
                {!this.props.race.randomize_team ? (
                    <div className="Join_Card">
                        <h5>Join {this.state.raceName}</h5>
                        <Form className="Join_Form">
                            <FormGroup>
                                <Label> First Name :</Label>
                                <Input 
                                onChange={this.onChange}
                                name="name"
                                value={this.state.name}
                                type="text" 
                                placeholder="Enter your First Name" />
                            </FormGroup>
                            <FormGroup >
                                <Label for="selectTeam"> Team: </Label>
                                 <Input 
                                 type="select"
                                 name="team"
                                 onChange={this.select}
                                 id ="selectTeam">
                                 {this.props.race.teams.map(team => {
                                    return <option key={team.id} value={team.id} name="team" >{team.name}</option> 
                                 })}
        
                                </Input>
                                <Button onClick ={this.handleClick}> Join the Race! </Button>
                            </FormGroup>
                        </Form>
                    </div> ) : (
                    <div className="Join_Card">
                        <Form className="Join_Form">
                            <FormGroup>
                            <Label> First Name :</Label>
                            <Input 
                                onChange={this.onChange}
                                name="name"
                                value={this.state.name}
                                type="text" 
                                placeholder="Enter your First Name" />
                                <Button onClick ={this.handleClick}> Join the Race! </Button>
                            </FormGroup>
                        </Form>
                    </div>
                )}
            </div> : null 
        );
    }
}

const mapStateToProps = state => {
    return {
        race: state.AdminDelivery.race,
        gotRace: state.AdminDelivery.gotRace,
        index: state.AdminDelivery.index
    }
}
export default connect(mapStateToProps, {createStudent}) (StudentJoinCard);