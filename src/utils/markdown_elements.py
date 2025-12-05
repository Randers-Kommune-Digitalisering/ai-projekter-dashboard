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
            .stAppToolbar {
                background-color: #FCFAF4;
            }
            .stApp, .stAppHeader, .stMainBlockContainer, .stBottom > div {
                background-color: #FFFEFA;
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

            /*.stSidebar p {
                color: #f0f0e8 !important;
            }*/

            [data-testid="stElementContainer"]:has(.overlay-header) {
                position: fixed;
                top: 0;
                left: 0;
                height: 3.75rem;
                width: 100vw;
                z-index: 999991;
                border-bottom: 1px solid #eee;
                pointer-events: none;
            }
            [data-testid="stElementContainer"]:has(.overlay-header) * {
                max-height: 3.75rem;
            }
            
            /* section.stSidebar[aria-expanded="true"] ~ div .appToolbarOverlay {
                left: 19rem;
                width: calc(100% - 19rem);
            } */
            .overlay-header {
                display: flex;
                align-items: center;
                padding-left: 1rem;
                height: 3.75rem;
            }
            .stAppToolbar {
                background-color: #FCFAF4;
            }
            .stApp, .stAppHeader, .stBottom > div {
                background-color: #FFFEFA;
            }



            .tag {
                background-color: #f0ede0;
                border-radius: 0.5rem;
                padding: 0.5rem 1rem;
                font-size: 0.95rem;
                width: fit-content;
                display: inline-block;
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
