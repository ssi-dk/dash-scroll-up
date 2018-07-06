import React, {Component} from 'react';
import PropTypes from 'prop-types';




/**
 * DashScrollUp adds a button 
 */
export default class DashScrollUp extends Component {
    constructor(props) {
        super(props)
        this.state = {hover: false}
    }

    toggleHover() {
        this.setState({ hover: !this.state.hover })
    }

    scrollStep() {
        if (window.pageYOffset === 0) {
            clearInterval(this.state.intervalId);
        }
        window.scroll(0, window.pageYOffset - this.props.scrollStepInPx);
    }

    scrollToTop() {
        let intervalId = setInterval(this.scrollStep.bind(this), this.props.delayInMs);
        this.setState({ intervalId: intervalId });
    }

    render() {
        const {id, label} = this.props;
        const scrollStyles = {
            width: '40px',
            height: '40px',
            position: 'fixed',
            bottom: '10px',
            right: '10px',
            padding: '0px'
        }
        if (this.state.hover) {
            scrollStyles.opacity = '1.0'
        } else {
            scrollStyles.opacity = '0.3'
        }
        return (
            <button id={id} title='Back to top' className='scroll'
                onClick={() => { this.scrollToTop(); }}
                style={{ ...scrollStyles, ...this.props.style }}
                className={this.props.className}
                onMouseEnter={this.toggleHover.bind(this)}
                onMouseLeave={this.toggleHover.bind(this)}>
                {/* <span className='arrow-up glyphicon glyphicon-chevron-up'></span> */}
                {label}
            </button>
        );
    }
}

DashScrollUp.propTypes = {
    /**
     * The ID used to identify this compnent in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * A label that will be printed when this component is rendered.
     */
    label: PropTypes.string.isRequired,

    /**
    * A object that contains the styles in react format.
    */
    style: PropTypes.object,

    /**
    * Class name to apply to the button
    */
    className: PropTypes.string,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func
};
