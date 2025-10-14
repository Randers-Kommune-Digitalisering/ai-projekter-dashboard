def get_custom_css():
    return """
        <style>
            .stAppToolbar {
                background-color: #FCFAF4;
            }
            .stApp, .stAppHeader, .stBottom > div {
                background-color: #FFFEFA;
            }

            @media (prefers-color-scheme: dark) {
                .stAppToolbar {
                    background-color: #27292b;
                }
                .stApp, .stAppHeader, .stBottom > div {
                    background-color: #222326;
                }
                .stMainBlockContainer {
                    background-color: #222326;
                }
            }
        </style>
    """
