function Navbar({ isLoggedIn, onLogout }) {


    return (
        <nav>
            <div className="header">

                <h2>Vendor Management System</h2>
                {isLoggedIn && (
                    <button onClick={onLogout}>
                        Logout
                    </button>
                )}
            
            </div>
        </nav>
    );
}

export default Navbar;