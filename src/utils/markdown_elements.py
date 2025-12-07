def get_custom_css():
    return """
        <style>
            .stMain {
                margin-top: 3.5rem;
                height: calc(100dvh - .5rem);
            }
            .stMainBlockContainer {
                padding-top: 1rem;
            }
            .stApp, .stAppHeader, .stMainBlockContainer, .stBottom > div {
                background-color: #FFFEFA;
            }
            .stAppToolbar {
                background-color: #fefdf1;
            }
            [data-testid="stElementContainer"]:has(.overlay-header) {
                position: fixed;
                top: 0;
                left: 0;
                height: 3.75rem;
                width: 100vw;
                z-index: 999991;
                border-bottom: 1px solid #e0ded3;
                pointer-events: none;
            }
            [data-testid="stElementContainer"]:has(.overlay-header) * {
                max-height: 3.75rem;
            }
            .stSidebar {
                z-index: 999992;
                border-right: 1px solid #e0ded3;
                background-color: #f0ede0;
            }
            section[data-testid="stSidebar"][aria-expanded="true"] {
                min-width: 15rem;
            }
            .stSidebar .stHeading h1 {
                padding-top: 0;
            }


            /* section.stSidebar[aria-expanded="true"] ~ div .appToolbarOverlay {
                left: 19rem;
                width: calc(100% - 19rem);
            } */

            
            div[data-testid="stLayoutWrapper"] > .stExpander > details {
                background-color: #b3c4a1;
                border: 0;
            }
            div[data-testid="stLayoutWrapper"] > .stExpander > details[open] {
                background-color: #FCFAF4;
                outline: 1px solid #c2d0b3;
            }
            div[data-testid="stLayoutWrapper"] > .stExpander > details[open] > summary {
                background-color: #c2d0b3;
            }
            div[data-testid="stLayoutWrapper"] > .stExpander > details > summary {
                padding: 1rem 0.8rem;
            }
            div[data-testid="stLayoutWrapper"]:hover > .stExpander > details > summary {
                background-color: #c2d0b3;
            }


            .tag {
                background-color: #f0ede0;
                border-radius: 0.5rem;
                padding: 0.8rem 1.2rem;
                font-size: 0.95rem;
                width: fit-content;
                display: inline-block;
            }
            .projects-flex-item {
                display: inline-block;
            }
            .projects-flex-item > div:first-child {
                font-size: 0.8em;
                color: #555555;
                font-weight: 600;
            }
            .projects-flex-item > div:last-child {
                padding-left: 0.2rem;
                padding-right: 0.2rem;
                padding-top: 0.5rem;
            }




            @media (prefers-color-scheme: dark) {
                .stAppToolbar {
                    background-color: #27292b;
                }
                .stApp, .stAppHeader, .stMainBlockContainer, .stBottom > div{
                    background-color: #222326;
                }

                .tag {
                    background: #27292b;
                }
            }
        </style>
    """
