<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <div class="toc-contents">
            <ul>
                <xsl:apply-templates/>
            </ul>
        </div>
    </xsl:template>
    <xsl:template match="Schritt">
        <li>
            <div class="toc-part">
                <ul>
                    <xsl:apply-templates />
                </ul>
            </div>
        </li>
    </xsl:template>
</xsl:stylesheet>